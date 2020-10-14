#6.5 String Slicing Assignmeent
text = "X-DSPAM-Confidence:    0.8475"

slice_start = text.find(":")
slice_text = float(text[slice_start+1:].strip())
print(slice_text)
