# 12. Steganography - Hide a Message (Extreme)

def hide_message(input_file, output_file, secret_message):
    # Copy original file to new file
    with open(input_file, 'rb') as infile, open(output_file, 'wb') as outfile:
        outfile.write(infile.read())
        # Append the secret message encoded as bytes
        outfile.write(secret_message.encode('utf-8'))
        
def extract_message(filepath, tail_size=128):
    # Read the end of the file where the message might be hidden
    with open(filepath, 'rb') as f:
        # Seek to the end minus tail_size bytes
        f.seek(0, 2)
        file_size = f.tell()
        
        seek_pos = max(0, file_size - tail_size)
        f.seek(seek_pos)
        tail_data = f.read()
        
        # In a real scenario, you'd use a delimiter or a fixed size header.
        # Here we'll just try to decode and print it, ignoring non-decodable bytes.
        try:
            # We know the message format for our basic steganography.
            # Let's find "SUPER_SECRET_KEY" in the decoded tail string.
            decoded_tail = tail_data.decode('utf-8', errors='ignore')
            if "SUPER_SECRET_KEY" in decoded_tail:
                idx = decoded_tail.find("SUPER_SECRET_KEY")
                print(f"Extracted Secret: {decoded_tail[idx:]}")
            else:
                print("No secret found.")
        except Exception as e:
            print(f"Error extracting message: {e}")

if __name__ == '__main__':
    msg = "SUPER_SECRET_KEY=42"
    hide_message('../data/image.jpg', '../data/secret_image.jpg', msg)
    print("Message hidden in data/secret_image.jpg")
    
    extract_message('../data/secret_image.jpg')
