#pip install colour
from colour import Color
from flask import Flask , request , jsonify , Response
from flask_api import FlaskAPI, status, exceptions
from flask_cors import CORS

app = FlaskAPI(__name__)
CORS(app)

"""
#FF0000 Red
#00FF00 Green
#0000FF Blue
#FFFFFF White
#C0C0C0 Silver
#800080 Purple
#FFFF00 Yellow
"""


class createPassword:
	"""
	Take the input string.
	Take the color value.
	"""

	def __init__(self , sentence ,color ):
		self.sentence = sentence
		self.color = color

	def trimSentence(self , sentence_split_list ):
		try:
			trimmed_sentence = []
			for index , each_word in enumerate(sentence_split_list):
				if index == 0:
					single_character = each_word[0].upper()
				else:
					single_character = each_word[0].lower()
				trimmed_sentence.append(single_character)
			trimmed_sentence = "".join(trimmed_sentence)	
			return(trimmed_sentence)
		except Exception as e:
			return 0


	def sentenceColorPassword(self):
		try:
			# split the sentence
			lower_case_sentence = self.sentence.lower()
			upper_case_sentence = self.sentence.upper()
			sentence_split = self.sentence.split()
			if self.trimSentence(sentence_split):
				trimmed_sentence = self.trimSentence(sentence_split)

			color = Color(self.color)
			generated_password = color.hex_l + trimmed_sentence + color.hex_l
			return ({"generated_password":generated_password , "trimmed_sentence":trimmed_sentence , "color_code": color.hex_l})
		except Exception as e:
			print("Error in core.py" , e)
			return 0

	def PasswordAndmetaData(self):
		"""
		return:
			password length
			color code
			deduced sentence password
			pattern of the password 
		"""
		try:
			
			
			password_details = self.sentenceColorPassword()
			if password_details:
				password_len = len(password_details["generated_password"])
				color_code = password_details["color_code"]
				trimmed_sentence = password_details["trimmed_sentence"]
				password_pattern = [password_details["color_code"] , password_details["trimmed_sentence"] , password_details["color_code"] ]
				
				return ({"generated_password":password_details["generated_password"] , 
						"password_length" : password_len , 
						"color_code" :color_code , 
						"trimmed_sentence":trimmed_sentence , 
						"password_pattern": password_pattern  })
			else:
				return 0
		except Exception as e:
			print("Error in meta data creation " , e)
			return 0

		
			



@app.route('/pass' , methods = ['POST']  )
def rempas():


	try:
		sentence = request.get_json()['sentence'] 
		color = request.get_json()['color']
	except Exception as e:
		status = 400
		message = "Client side Error"
		password = None
		jsonOut = jsonify(status = status , message = message , password = password)
		return jsonOut

	try:
		create_pass = createPassword(sentence = sentence, color = color)
		password = create_pass.PasswordAndmetaData()
		password["sentence"] = sentence
		password["color"] = color
		status = 200
		message = "Success"
	except Exception as e:
		status = 500
		message = "Server side Error"
		password = None

	jsonOut = jsonify(status = status , message = message , password = password)
	return jsonOut




if __name__ == '__main__':
	# app.run(host = '0.0.0.0',debug=True)
	app.run()

