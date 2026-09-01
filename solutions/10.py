# 10. Chunked File Copy (Intermediate)

def copy_in_chunks(input_file, output_file, chunk_size=1024):
    with open(input_file, 'rb') as infile, open(output_file, 'wb') as outfile:
        while True:
            chunk = infile.read(chunk_size)
            if not chunk: # EOF reached
                break
            outfile.write(chunk)

if __name__ == '__main__':
    copy_in_chunks('../data/image.jpg', '../data/image_copy.jpg')
    print("Copied image.jpg to image_copy.jpg in chunks")
