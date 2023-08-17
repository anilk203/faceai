# create docker network
docker network create deep_ai_network

# client

##### Create images directory under client and place the images to register

##### Register faces (single or multiple):
```
cd client
mkdir images
```

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


```
python register-faces.py

```

##### Recognize faces (single):
open the recognize-faces.py file and replace IMAGE_NAME_WITH_EXTENSION with file.

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
##### create a folder recoginze under / 
```
docker exec -it faceaiapp bash
cd /
mkdir recognize
```

##### http://localhost:10000

