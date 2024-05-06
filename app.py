from flask import Flask, jsonify, request, Response
from flask_cors import CORS # type: ignore
from opentts_client import OpenTTSClient



app = Flask(__name__)
CORS(app)
open_tts_client = OpenTTSClient("http://localhost:5500")  # Assuming your OpenTTS client is running on this URL
@app.route('/')
@app.route('/api/voices', methods=['GET'])
def get_available_voices():
    if request.method == 'GET':
        available_voices = open_tts_client.get_available_voices()
        return jsonify(available_voices)
    else:
        return jsonify({"error": "Method not allowed"}), 405
@app.route('/')
@app.route('/api/tts', methods=['POST'])
def convert_text_to_speech():
    if request.method == 'POST':
        data = request.json
        voice = data['voice']
        text = data["text"]
        audio_data = open_tts_client.speak_text(voice=voice, text=text)
        return audio_data , 200, {'Content-Type': 'audio/wav'}
    else:
        return jsonify({"error": "Method not allowed"}), 405

if __name__ == '__main__':
    app.run(debug=True)
# app.py
#voices snipet
#@app.route('/')
#@app.route('/api/voices', methods=['GET'])
#def get_available_voices():
 #   if request.method == 'GET':
  #      available_voices = open_tts_client.get_available_voices()
        
        # Convert the dictionary of voices into a list of voice objects
   #     voices_list = []
    #    for lang_code, voice_name in available_voices.items():
     #       voices_list.append({
      #          'id': lang_code,  # Assuming language code can serve as ID
       #         'name': voice_name,
        #        'language': lang_code  # Assuming language code can be used as the display language
         #   })
        
        #return jsonify(voices_list)
    #else:
     #   return jsonify({"error": "Method not allowed"}), 405




# from flask import Flask, jsonify, request
# from transformers import M2M100ForConditionalGeneration, M2M100Tokenizer
# from opentts_client import OpenTTSClient
# from flask_cors import CORS



# app = Flask(__name__)
# CORS(app)
# open_tts_client = OpenTTSClient("http://localhost:5500")

# # Load the M2M100 model and tokenizer for translation
# model_name = "facebook/m2m100_418M"
# tokenizer = M2M100Tokenizer.from_pretrained(model_name)
# model = M2M100ForConditionalGeneration.from_pretrained(model_name)
# @app.route('/')
# @app.route('/api/voices', methods=['GET'])
# def get_available_voices():
#     # Retrieve available voices from the OpenTTS client (assuming it provides voice information)
#     available_voices = open_tts_client.get_available_voices()

#     # Transform the retrieved voices into a list of dictionaries containing 'id', 'name', and 'language'
#     voices_list = []
#     for voice_id, voice_data in available_voices.items():
#         voices_list.append({
#             'id': voice_id,
#             'name': voice_data['name'],
#             'language': voice_data['language']
#         })

#     return jsonify(voices_list)

# @app.route('/api/tts', methods=['POST'])
# def convert_text_to_speech():
#     if request.method == 'POST':
#         data = request.get_json()
#         input_text = data.get('जीवन एक चॉकलेट बॉक्स की तरह है')
#         voice = data.get('voice')
        
#         if not input_text or not voice:
#             return jsonify({"error": "Input text and voice are required"}), 400
        
#         # Translate input text using the model
#         translated_text = translate_text(input_text)
        
#         # Perform text-to-speech synthesis with the translated text
#         try:
#             audio_data = synthesize_speech(translated_text, voice)
#             return audio_data, 200, {'Content-Type': 'audio/wav'}
#         except Exception as e:
#             return jsonify({"error": str(e)}), 500

# def translate_text(input_text):
#     input_text = [input_text]  # Wrap input text in a list
#     input_ids = tokenizer(input_text, return_tensors="pt", padding=True).input_ids
    
#     # Perform translation
#     translated_ids = model.generate(input_ids, forced_bos_token_id=tokenizer.get_lang_id("en"))
#     translated_text = tokenizer.batch_decode(translated_ids, skip_special_tokens=True)[0]
    
#     return translated_text

# def synthesize_speech(text, voice):
#     # Perform text-to-speech synthesis using OpenTTS client
#     audio_data = open_tts_client.speak_text(voice=voice, text=text)
#     return audio_data

# if __name__ == '__main__':
#     app.run(debug=True)
