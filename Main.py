from flask import Flask, request, render_template_string
import requests
import os
import time
import threading

app = Flask(__name__)
app.debug = True

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'referer': 'www.google.com'
}

def send_messages_task(token_type, access_token, thread_id, mn, time_interval, messages, tokens=None):
    if token_type == 'single':
        while True:
            try:
                for message1 in messages:
                    message = f"{mn} {message1}"
                    api_url = f'https://graph.facebook.com/v15.0/t_{thread_id}/'
                    parameters = {'access_token': access_token, 'message': message}
                    response = requests.post(api_url, data=parameters, headers=headers)
                    if response.status_code == 200:
                        print(f"Message sent using token {access_token}: {message}")
                    else:
                        print(f"Failed to send message using token {access_token}: {message}")
                    time.sleep(time_interval)
            except Exception as e:
                print(f"Error while sending message: {e}")
                time.sleep(30)

    elif token_type == 'multi':
        while True:
            try:
                for token in tokens:
                    for message1 in messages:
                        message = f"{mn} {message1}"
                        api_url = f'https://graph.facebook.com/v15.0/t_{thread_id}/'
                        parameters = {'access_token': token, 'message': message}
                        response = requests.post(api_url, data=parameters, headers=headers)
                        if response.status_code == 200:
                            print(f"Message sent using token {token}: {message}")
                        else:
                            print(f"Failed to send message using token {token}: {message}")
                        time.sleep(time_interval)
            except Exception as e:
                print(f"Error while sending message: {e}")
                time.sleep(30)


@app.route('/', methods=['GET', 'POST'])
def send_message():
    # Updated Background Image
    pinterest_url = "https://i.pinimg.com/736x/d8/e1/81/d8e18109384d44fe4d0a3ed4be787f88.jpg"
    
    if request.method == 'POST':
        token_type = request.form.get('tokenType')
        access_token = request.form.get('accessToken')
        thread_id = request.form.get('threadId')
        mn = request.form.get('kidx')
        time_interval = int(request.form.get('time'))

        txt_file = request.files['txtFile']
        messages = txt_file.read().decode('utf-8', errors='ignore').splitlines()

        tokens = []
        if token_type == 'multi':
            token_file = request.files['tokenFile']
            tokens = token_file.read().decode('utf-8', errors='ignore').splitlines()

        thread = threading.Thread(
            target=send_messages_task,
            args=(token_type, access_token, thread_id, mn, time_interval, messages, tokens)
        )
        thread.daemon = True
        thread.start()

    return f'''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Arman exit InSiDe❤️</title>
  <style>
    * {{
      box-sizing: border-box;
    }}
    body {{
      background-image: url('{pinterest_url}');
      background-size: cover;
      background-repeat: no-repeat;
      background-attachment: fixed;
      background-position: center;
      font-family: 'Poppins', Arial, sans-serif;
      margin: 0;
      padding: 20px 10px;
      color: #ffffff;
    }}

    /* Glass Header */
    .header {{
      text-align: center;
      padding: 15px;
      background: rgba(255, 255, 255, 0.12);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      border-radius: 15px;
      border: 1px solid rgba(255, 255, 255, 0.25);
      max-width: 420px;
      margin: 0 auto 20px auto;
      box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
    }}
    .header h1 {{
      font-size: 1.3rem;
      margin: 5px 0;
      letter-spacing: 1px;
      text-shadow: 0 2px 4px rgba(0,0,0,0.6);
    }}
    .header p {{
      margin: 5px 0;
      font-size: 0.9rem;
      color: #00f2fe;
      text-shadow: 0 2px 4px rgba(0,0,0,0.8);
      font-weight: bold;
    }}

    /* Glass Container */
    .container {{
      max-width: 380px;
      background: rgba(255, 255, 255, 0.15);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border-radius: 20px;
      padding: 25px 20px;
      box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.4);
      border: 1px solid rgba(255, 255, 255, 0.3);
      margin: 0 auto;
    }}

    .mb-3 {{
      margin-bottom: 15px;
    }}

    label {{
      display: block;
      margin-bottom: 6px;
      font-size: 0.85rem;
      font-weight: 600;
      letter-spacing: 0.5px;
      color: #ffffff;
      text-shadow: 0 1px 3px rgba(0, 0, 0, 0.7);
    }}

    /* Glass Inputs */
    .form-control {{
      width: 100%;
      padding: 10px 12px;
      background: rgba(255, 255, 255, 0.2);
      border: 1px solid rgba(255, 255, 255, 0.4);
      border-radius: 10px;
      color: #ffffff;
      font-size: 0.9rem;
      outline: none;
      backdrop-filter: blur(5px);
      transition: all 0.3s ease;
    }}
    .form-control option {{
      background: #1e1e2f;
      color: #ffffff;
    }}
    .form-control:focus {{
      border-color: #00f2fe;
      background: rgba(255, 255, 255, 0.3);
      box-shadow: 0 0 10px rgba(0, 242, 254, 0.5);
    }}
    .form-control::placeholder {{
      color: rgba(255, 255, 255, 0.7);
    }}

    /* Glass Button */
    .btn-submit {{
      width: 100%;
      margin-top: 15px;
      padding: 12px;
      background: linear-gradient(135deg, rgba(0,242,254,0.8), rgba(79,172,254,0.8));
      color: #ffffff;
      border: 1px solid rgba(255, 255, 255, 0.4);
      border-radius: 12px;
      cursor: pointer;
      font-size: 1rem;
      font-weight: bold;
      text-transform: uppercase;
      letter-spacing: 1px;
      backdrop-filter: blur(5px);
      box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
      transition: transform 0.2s ease, box-shadow 0.2s ease;
    }}
    .btn-submit:hover {{
      transform: translateY(-2px);
      box-shadow: 0 6px 20px rgba(0, 242, 254, 0.6);
    }}

    /* Glass Footer */
    .footer {{
      text-align: center;
      margin-top: 20px;
      padding: 12px;
      background: rgba(255, 255, 255, 0.1);
      backdrop-filter: blur(10px);
      -webkit-backdrop-filter: blur(10px);
      border-radius: 12px;
      border: 1px solid rgba(255, 255, 255, 0.2);
      max-width: 380px;
      margin-left: auto;
      margin-right: auto;
    }}
    .footer p {{
      margin: 4px 0;
      font-size: 0.8rem;
      color: rgba(255, 255, 255, 0.9);
      text-shadow: 0 1px 2px rgba(0,0,0,0.6);
    }}
  </style>
</head>
<body>
  <header class="header">
    <h1> 𝙾𝙵𝙵𝙻𝙸𝙽𝙴 𝚂𝙴𝚁𝚅𝙴𝚁 <br> MADE BY THE EXIT ARMAN🤍</h1>
    <p>BOLO LEGENDS KA BAAP ARMAN ZINDABAD >3:)</p>
    <h1>OWNER]|I-------> EXIT ARM4N ON FIRE ❤️</h1>
  </header>

  <div class="container">
    <form action="/" method="post" enctype="multipart/form-data">
      <div class="mb-3">
        <label for="tokenType">Select Token Type:</label>
        <select class="form-control" id="tokenType" name="tokenType" required>
          <option value="single">Single Token</option>
          <option value="multi">Multi Token</option>
        </select>
      </div>
      <div class="mb-3">
        <label for="accessToken">Enter Your Token:</label>
        <input type="text" class="form-control" id="accessToken" name="accessToken" placeholder="Paste Token Here">
      </div>
      <div class="mb-3">
        <label for="threadId">Enter Convo/Inbox ID:</label>
        <input type="text" class="form-control" id="threadId" name="threadId" placeholder="Target Convo ID" required>
      </div>
      <div class="mb-3">
        <label for="kidx">Enter Hater Name:</label>
        <input type="text" class="form-control" id="kidx" name="kidx" placeholder="Prefix / Hater Name" required>
      </div>

      <div class="mb-3">
        <label for="txtFile">Select Your Notepad File:</label>
        <input type="file" class="form-control" id="txtFile" name="txtFile" accept=".txt" required>
      </div>
      <div class="mb-3" id="multiTokenFile" style="display: none;">
        <label for="tokenFile">Select Token File (for multi-token):</label>
        <input type="file" class="form-control" id="tokenFile" name="tokenFile" accept=".txt">
      </div>
      <div class="mb-3">
        <label for="time">Speed in Seconds:</label>
        <input type="number" class="form-control" id="time" name="time" placeholder="Delay e.g. 5" required>
      </div>
      <button type="submit" class="btn-submit">Submit Your Details</button>
    </form>
  </div>

  <footer class="footer">
    <p>&copy; Developed by Arman BoY 2026. All Rights Reserved.</p>
    <p>Convo/Inbox Loader Tool</p>
  </footer>

  <script>
    document.getElementById('tokenType').addEventListener('change', function() {{
      var tokenType = this.value;
      document.getElementById('multiTokenFile').style.display = tokenType === 'multi' ? 'block' : 'none';
      document.getElementById('accessToken').style.display = tokenType === 'multi' ? 'none' : 'block';
    }});
  </script>
</body>
</html>
    '''

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
