from invoke import task


@task
def mig(c):
    c.run("python manage.py makemigrations")


@task
def upg(c):
    c.run("python manage.py migrate")


@task
def admin(c):
    c.run("python manage.py createsuperuser")


@task
def apps(c):
    c.run("python manage.py startapp apps")


@task
def load(c):
    c.run("python manage.py loaddata  user.json adminsetting.json products.json categories.json regions.json disdricts.json")


@task
def dump(c):
    c.run("python manage.py dumpdata apps.adminsetting > adminsetting.json")
