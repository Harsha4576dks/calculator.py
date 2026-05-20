 #python-basics

class Family():
    def main(self):

        while True:
            members = input("Enter age of the family member:")

            if members == "exit":
                print("thankyou")
                break
            members = int(members)

            if members in range(5,20):
                print("child")

            elif members in range(20,40):
                print("adult")

            elif members in range(40,60):
                print("more than an adult")

            elif members in range(60,80):
                print("old")

            else:
                print("oldest")

c1 = Family()
c1.main() 


