from ..crud import crud


# test
todoSystem = crud.System()
todoSystem.create("watermelon")
todoSystem.create("pineapple")
todoSystem.create("pineapple")
todoSystem.create("carrot")
todoSystem.delete("watermelon")
todoSystem.create("celery")
todoSystem.update("celery", "CELLLLLLLLRYYYY")
todoSystem.read()