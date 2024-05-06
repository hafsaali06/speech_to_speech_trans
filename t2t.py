# from transformers import M2M100ForConditionalGeneration, M2M100Tokenizer

# hi_text = "जीवन एक चॉकलेट बॉक्स की तरह है।"
# chinese_text = "生活就像一盒巧克力。"

# model = M2M100ForConditionalGeneration.from_pretrained("facebook/m2m100_418M")
# tokenizer = M2M100Tokenizer.from_pretrained("facebook/m2m100_418M")

# # translate Hindi to French
# tokenizer.src_lang = "hi"
# encoded_hi = tokenizer(hi_text, return_tensors="pt")
# generated_tokens = model.generate(**encoded_hi, forced_bos_token_id=tokenizer.get_lang_id("en"))
# result = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
# print(result)
# # => "La vie est comme une boîte de chocolat."

# # translate Chinese to English
# tokenizer.src_lang = "zh"
# encoded_zh = tokenizer(chinese_text, return_tensors="pt")
# generated_tokens = model.generate(**encoded_zh, forced_bos_token_id=tokenizer.get_lang_id("en"))
# tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
# # => "Life is like a box of chocolate."





# from transformers import pipeline, M2M100Tokenizer, M2M100ForConditionalGeneration

# # Instantiate the M2M100 tokenizer
# tokenizer = M2M100Tokenizer.from_pretrained("facebook/m2m100_418M")

# # Instantiate the PyTorch version of M2M100 model for conditional generation
# model = M2M100ForConditionalGeneration.from_pretrained("facebook/m2m100_418M")

# # Set up the pipeline for text-to-text generation
# pipe = pipeline(task='text2text-generation', model=model, tokenizer=tokenizer)

# # Provide the input text and specify the language for the output
# result = pipe("जीवन एक चॉकलेट बॉक्स की तरह है।", forced_bos_token_id=tokenizer.get_lang_id(lang="en"))
# print(result)



# from transformers import pipeline, M2M100Tokenizer, M2M100ForConditionalGeneration
# # from your_text_to_speech_module import text_to_speech_function  # Import your text-to-speech function

# # Instantiate the M2M100 tokenizer
# tokenizer = M2M100Tokenizer.from_pretrained("facebook/m2m100_418M")

# # Instantiate the PyTorch version of M2M100 model for conditional generation
# model = M2M100ForConditionalGeneration.from_pretrained("facebook/m2m100_418M")

# # Set up the pipeline for text-to-text generation
# pipe = pipeline(task='text2text-generation', model=model, tokenizer=tokenizer)

# # Provide the input text in Hindi and specify the desired output language (English)
# input_text = "जीवन एक चॉकलेट बॉक्स की तरह है।"
# output_lang_id = tokenizer.get_lang_id(lang="en")
# generated_text = pipe(input_text, forced_bos_token_id=output_lang_id)[0]['generated_text'].strip()
# print(generated_text)
#   # Call your text-to-speech function with the generated text as input



from transformers import pipeline, M2M100Tokenizer, M2M100ForConditionalGeneration

# Instantiate the M2M100 tokenizer
tokenizer = M2M100Tokenizer.from_pretrained("facebook/m2m100_418M")

# Instantiate the PyTorch version of M2M100 model for conditional generation
model = M2M100ForConditionalGeneration.from_pretrained("facebook/m2m100_418M")

# Function to generate text in the desired language
def generate_text(output_lang="en"):
    # Prompt the user to enter the input text
    input_text = input("Enter the text in Hindi: ")

    # Get language ID for the desired output language
    output_lang_id = tokenizer.get_lang_id(lang=output_lang)
    
    # Use the pipeline to generate text
    generated_text = pipeline(task='text2text-generation', model=model, tokenizer=tokenizer)(input_text, forced_bos_token_id=output_lang_id)[0]['generated_text'].strip()
    
    return generated_text

# Example usage of the generate_text function
def main():
    output_lang = "en"  # Desired output language
    generated_text = generate_text(output_lang)
    print("Generated Text (in English):", generated_text)

if __name__ == "__main__":
    main()



