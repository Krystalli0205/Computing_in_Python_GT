#Write a function called redeobfuscate. This function should
#take two parameters, both strings. The first string is the
#filename of a file to which to write (output_file), and the
#second string is the filename of a file from which to read
#(input_file).
#
#deobfuscate should copy the contents of input_file into
#output_file, with one twist: every triplet of characters
#should be reversed. So, if the original file contained the
#text:
#
# CBAGFE
#
#Then the output file would contain the text ABCDEFG: CBA
#becomes ABC and GFE becomes EFG. Note that for this problem,
#you may assume that the number of characters is guaranteed
#to be a multiple of 3, so you don't have to worry about
#handling any left over characters.
#
#This change should be applied to every character in the
#file: punctuation, spaces, and even line breaks. So, if the
#original file was:
#
# abc def ghi jkl
# mno pqr stu vw
#
#Then the output file would contain:
#
# cbaed g f ihlkjnm
# p o rquts wv
#
#Notice that the second triplet is originally " de", and it
#becomes "ed ", with the space at the end. Notice also that
#one of the triplets is "\nmn", with the line break at the
#end of line as the first character; so, when it rotates,
#the n and m come first, followed by the line break.
#
#We've included two files for you to test on: anInputFile.txt
#and anOutputFile.txt. The test code below will copy the text
#from the first file to the second. Feel free to modify the
#first to test different setups.
#
#HINT: Spaces and linebreaks are NOT special cases. Treat them
#as any other character to make this easier!


#Write your function here!

def redeobfuscate(output_file, input_file):
    input = open(input_file, "r")
    output = open(output_file, "w")
    content = input.read()
    
    processed = ""
    for i in range(0, len(content), 3):
        triplet = content[i:i+3]
        processed += triplet[::-1]
    
    output.write(processed)
    output.close()
    input.close()




#The code below will test your function. You can find the two
#files it references in the drop-down in the top left. If your
#code works, anOutputFile.txt should have the text:
#I'm a Ramblin' Wreck
#from Georgia Tech
redeobfuscate("anOutputFile.txt", "anInputFile.txt")
print("Done running! Check anOutputFile.txt for the result.")


#If you accidentally erase anInputFile.txt, here's its original
#text to copy back in:
#m'I a maRilb 'nerW                                                                                                                                                                         
#kcorfG mroeaigeT !hc
