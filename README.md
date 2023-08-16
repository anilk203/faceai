# create docker network
docker network create deep_ai_network

# client

config.json - list of images can be registered with name.

```
ex: 
{
	"uploads": [
		{
			"file_name": "file1.jpg",
			"face_name": "apple"
		},
		{
			"file_name": "file2.jpg",
			"face_name": "banana"
		}
	]
}
```

Register faces (single or multiple):

```
python register-faces.py

```

Recognize faces (single):

```
python recognize-faces.py

```

# mysql

```
docker-compose up -d

```

Once mysql is up and running. Create a database name <faceaidb>

```
create database faceaidb;
```

Run the create table statements from create.sql 


# faceai

Default image is pulled for ARM, update based on your requirements.
##### docker-compose.yml,  image: deepquestai/deepstack:arm64

```
docker-compose up -d

```

# faceaiapp

Default ports can be updated in docker-compose.yml
##### web: 10000:5000

```
docker-compose up -d

```

##### http://localhost:10000

