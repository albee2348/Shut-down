def shutdown():
    choice = input("Do you want to shut down? ")

    if choice == "Yes":
        print("Shutting down")
    elif choice == "No":
        print("Abort shutdown")
    else:
        print("Sorry")

shutdown()