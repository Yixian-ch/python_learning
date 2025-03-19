from rss_reader import *
# libraries used in following function must be imported otherwise python can not know them
def walk_os(path: str) -> list[str]:
    if os.path.isfile(path):
        if path.suffix == ".xml":
            return [path]
        else:
            return []
    result = []
    for file in os.listdir(path):
        file = os.path.join(path,file)
        if os.path.isfile(file) and file[-4:] == ".xml":
            result.append(file)
        elif os.path.isdir(file):
            result.extend(walk_os(file))
    return result

def walk_pathlib(path: str) -> list[str]:
    filepath = Path(path)

    if filepath.is_file(): # if the path is a single file
        if filepath.suffix == ".xml":
            return [path]
        else:
            return []

    files = sorted(filepath.iterdir()) # returns what are in the directory, they can be a file or a directory

    if len(files) == 0:
        return []

    result = []
    for file in files:
        if file.is_file() and file.suffix == ".xml":
            result.append(str(file))
        elif file.is_dir():
            result.extend(str(file) for file in walk_pathlib(file))
    return result


def walk_glob(path: str) -> list[str]:
    return sorted(str(filepath) for filepath in Path(path).glob("**/*.xml"))


def filtre_vrai(article: dict) -> bool:
    return True


def create_filter_start_date(start: str) -> Callable[[dict], bool]:
    start_date = datetime.strptime(start, "%d/%m/%y")
    def filtre(a: dict) -> bool:
        try:
            d = datetime.strptime(" ".join(a['date'].split()[:4]), '%a, %d %b %Y')
        except ValueError:
            try:
                d = datetime.strptime(" ".join(a['date'].split()[:4]), '%a, %d %b %y')
            except ValueError:
                # date non valide, on écarte l'article
                return False
        return start_date <= d # on retourne vrai si tous les articles sont a partir de la date donnée
    return filtre


def create_filter_categories(categories: list[str]) -> Callable[[dict], bool]:
    cat_set = set(categories)
    def filtre(a: dict) -> bool:
        return len(cat_set.intersection(a['categories'])) > 0
    return filtre

def create_filter_source(source:str) -> Callable[[dict],bool]:
    def filtre(a:dict) -> bool:
        return source.lower() in a['source'].lower()
    return filtre

def build_filters(args: argparse.Namespace) -> list[Callable[[dict], bool]]:
    filtres = []
    if args.start:
        f = create_filter_start_date(args.start)
        filtres.append(f)
    if len(args.categories) > 0:
        f = create_filter_categories(args.categories)
        filtres.append(f)
    if args.source:
        f = create_filter_source(args.source)
        filtres.append(f)
    return filtres


def filtrage(filtres: list[Callable[[dict], bool]], articles: list[dict]) -> list[dict]:
    resultat = []
    for a in articles:
        if all([f(a) for f in filtres]):
            resultat.append(a)
    return resultat


def main():
    parser = argparse.ArgumentParser(description="teamwork never die")

    parser.add_argument("rss_feed")
    parser.add_argument("-r", "--reader", choices=("re", "etree", "feedparser"))
    parser.add_argument("-w", "--directory-walker", choices=("os", "pathlib", "glob"))
    parser.add_argument("-s", "--start", help="date à partir de laquelle on conserve les articles: 01/02/25 format accepté")
    parser.add_argument("-c", "--categories", nargs="*")
    parser.add_argument("--source")
    args = parser.parse_args()

    if args.categories is None:
        args.categories = []

    walker = name_to_walker.get(args.directory_walker) # use the input walker as the key to search in the dict which walker to use
    # walker is a function
    if walker is None:
        raise ValueError(f"Invalid value for directory walker: {args.directory_walker}")
    
    # same logic
    reader = name_to_reader.get(args.reader)
    if reader is None:
        raise ValueError(f"Invalid value for RSS reader: {args.reader}")

    files = walker(args.rss_feed) # rss_feed is the path and walker here is one of the three functions re, etree or feedparser 

    articles = []
    for feed in files:
        articles.extend(reader(feed))

    # filtrage
    filtres = build_filters(args)
    articles = filtrage(filtres, articles)

    for article in articles:
        for key in ("id", "source", "title", "description", "date", "categories"):
            print(key, ":", article[key])
        print()


name_to_reader = {
    "re": rss_reader_re,
    "etree": rss_reader_etree,
    "feedparser": rss_reader_feedparser
}

name_to_walker = {
    "os": walk_os,
    "pathlib": walk_pathlib,
    "glob": walk_glob
}


if __name__ == "__main__":
    main()

