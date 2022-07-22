# VideoUploader Project

## steps to folllow through 


1. clone the the repo to your local device

2. go to root directoru of project and run 
3. > `pip install -r reuirements.txt`

4. now run

5. >`python manage.py runserver`



## API DOCS

### post video

* endpoint= http://127.0.0.1:8000/video/create
* method = Post
* fields = {
    "title":str
    "type":str
    "video":file
}
* content-type : multipart form data

### list video

* endpoint= http://127.0.0.1:8000/video/list?date=2022-07-22T06:20:02.095293Z&type=ewrerewr

* method = get
* fields = {
    "date":str[optional return video at that date]
    "type":str[type]
    "less_than_time":str[return video less than given secs]
}


### check pricing
 
 * endpoint= http://127.0.0.1:8000/video/check?length=690&size=600&type=dsa

* method = get
* fields = {
    "size":str[in mb]
    "type":str
    "length":str[in secs]
}


