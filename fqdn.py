import subprocess
def run_nslookup(domain): 
    try: 
        result = subprocess.run(['nslookup', domain], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e: 
        return f"Error looking up {domain}: {e}" 
      
  def process_domains_file(file_path=None, output_path=None):
    if not file_path:
        file_path = input("Enter the path to the domain file: ")
    if not output_path:
        output_path = input("Enter the path for the output file: ")
    try: 
        with open(file_path, 'r') as file, open(output_path, 'w') as outfile:
            for line in file: 
                domain = line.strip()
                if domain:
                    output = run_nslookup(domain)
                    result_text = f"NSLOOKUP results for {domain}:\n{output}\n"
                    print(result_text)
                    outfile.write(result_text)
    except FileNotFoundError:
        print(f"Error: File not found: {file_path}") 

if __name__ == "__main__":
    file_path = input("Enter the path to the domain file: ")
    output_path = input("Enter the path for the output file: ")
    process_domains_file(file_path, output_path)
