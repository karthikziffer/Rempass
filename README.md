# Rempass


![Screenshot-from-2019-10-29-14-46-45.png](https://i.postimg.cc/28sHbmkc/Screenshot-from-2019-10-29-14-46-45.png)


This is a website to generate secured password with simple text inputs. The input is a sentence of user's choice and color. Using this two information, a secured password by concatenating trimmed sentence and color code is generated. This makes the password very strong to break. The authentication is ensured by the lenght of the sentence. Through this sentence, the user can remember his password better. Hence there is no tradeoff between a simple password to remember and it's authenticity. 

In the future release, deep learning based sequence networks can be employed to generate strong and rememberable passwords. The only shortcoming in developing such a model is training data. Currently, I am working on that and looking for volunteering for the same. 



---



### Python API


The backend is built using Python Flask Framework and currently hosted in heroku. Your are free to use the API by following below POST request. 



#### Endpoint
```
https://rempas-flask.herokuapp.com/pass
```


#### Body
```
{
	"sentence":"i am a hero" ,
	"color":"blue"
}
```

#### Response
```
{
    "message": "Success",
    "password": {
        "color": "blue",
        "color_code": "#0000ff",
        "generated_password": "#0000ffIaah#0000ff",
        "password_length": 18,
        "password_pattern": [
            "#0000ff",
            "Iaah",
            "#0000ff"
        ],
        "sentence": "i am a hero",
        "trimmed_sentence": "Iaah"
    },
    "status": 200
}
```


The average response time is 400ms.

---



<br>

### Webpage 

![Screenshot-from-2019-10-29-11-49-57.png](https://i.postimg.cc/kMHhxWMg/Screenshot-from-2019-10-29-11-49-57.png)



<br>


![Screenshot-from-2019-10-29-11-50-47.png](https://i.postimg.cc/gcyH0Rw7/Screenshot-from-2019-10-29-11-50-47.png)







