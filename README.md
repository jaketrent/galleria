## To run the webapp

```
./setup_env.sh
pipenv shell
pipenv install
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## No pipenv

If pipenv is not found, try:

```
python -m pipenv
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
./setup_env.sh
pipenv shell
./upload -s 900 -d "galleria/dirname" file1.jpg file2.jpg
./post -c Posters url1
```

Or combine:

```
./upload -s 900 -d "galleria/posters" file1.jpg file2.jpg | xargs ./post -c Posters
```

To post images already on the cdn:

```
aws s3 ls s3://cdn.jaketrent.com/<bucket_path>/ --profile cdnpoweruser | sed 's/.*\ //' | awk '{print "https://cdn.jaketrent.com/<bucket_path>/"$1}' | xargs ./post.py -c "<Collection Title>" -u "https://galleria.jaketrent.com/api/works/"
```

