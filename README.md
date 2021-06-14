## To run the webapp

```
pipenv shell
pipenv install
python manage.py migrate
python manage.py runserver
```

## To set up the cli

Use `aws configure` or create `~/.aws/credentials` file:

```
[default]
aws_access_key_id=abc123
aws_secret_access_key=abc123
```

Generate a galleria api access token:

Go to `/admin/authtoken/tokenproxy/add/` and "SAVE" for desired user.

Populate in `cli/.env`:

```
GALLERIA_API_TOKEN=abc123
```

To convert .HEIC files:

```
pipenev shell
brew install imagemagick
pipenv install

heic-to-jpg -s .
```

## To run the cli

```
pipenv shell
./upload -s 900 -d "galleria/dirname" file1.jpg file2.jpg
./post -c Posters url1
```

Or combine:

```
./upload -s 900 -d "galleria/posters" file1.jpg file2.jpg | xargs ./post -c Posters
```


