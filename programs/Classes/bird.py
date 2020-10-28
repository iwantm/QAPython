from abc import abstractmethod


class Bird:
    fly = True

    def noise(self):
        print('Birdnoise')

    babies = 0

    def reproduce(self):
        self.babies += 1

    @abstractmethod
    def eat(self):
        pass

    extinct = False


class Owl(Bird):
    def reproduce(self):
        self.babies += 6

    def eat(self):
        print('Peck Peck')


class Dodo(Bird):
    Fly = False
    extinct = True

    def eat(self):
        print("Nom Nom")

    def reproduce(self):
        if self.extinct == False:
            self.babies += 1
        else:
            print("No more dodos")
