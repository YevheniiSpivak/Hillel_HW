class Company:

    def __init__(self, name: str, country: str, address: str, workers: int, edrpou: int = None):
        self.name = name
        self.country = country
        self.address = address
        self.workers = workers
        self.edrpou = edrpou

    def info(self):
        print(f'Name: {self.name}\n'
              f'Country: {self.country}\n'
              f'Workers: {self.workers}\n')

    def add_workers(self, worker):
        self.workers = self.workers + worker


toyota = Company('Toyota Motor Corporation', 'Japan',
                 '2-1 Toyoda-cho, Kariya-shi, Aichi 448-8671 Japan MAP', 366_283)

toyota.info()
toyota.add_workers(100)
toyota.info()

