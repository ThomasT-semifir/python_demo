from inputs import get_user_input
import module_2 as mod

def main():
    entree = get_user_input("donne moi ton nom? ")
    print(entree)

    mod.test1()
    mod.test2()
    mod.test3()

if __name__ == "__main__":
    main()