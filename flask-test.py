from flask import Flask
import openai

openai.api_key = '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'

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo", 
  messages=[{"role": "user", "content": "Tell the world about the ChatGPT API in the style of a pirate."}]
)

print(completion)

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '''
      <!DOCTYPE html>
    <html lang="ko">
      <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <!-- 위 3개의 메타 태그는 *반드시* head 태그의 처음에 와야합니다; 어떤 다른 콘텐츠들은 반드시 이 태그들 *다음에* 와야 합니다 -->
        <title>부트스트랩 101 템플릿</title>

        <!-- 부트스트랩 -->
        <!-- 합쳐지고 최소화된 최신 CSS -->
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css">

        <!-- 부가적인 테마 -->
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap-theme.min.css">

        <!-- 합쳐지고 최소화된 최신 자바스크립트 -->
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/js/bootstrap.min.js"></script>

        <!-- IE8 에서 HTML5 요소와 미디어 쿼리를 위한 HTML5 shim 와 Respond.js -->
        <!-- WARNING: Respond.js 는 당신이 file:// 을 통해 페이지를 볼 때는 동작하지 않습니다. -->
        <!--[if lt IE 9]>
          <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
          <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
        <![endif]-->
      </head>
      <body>
        
        <div class="card">
            <div class="card-header">
              Chatting2
            </div>
            <div class="card-body">
              <blockquote class="blockquote mb-0">
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante.</p>
                <h1 class="text-dark">Chatting</h1>
          <hr>
          <div class="input-group">
            <div class="input-group-prepend">
              <span class="input-group-text">Input Text</span>
            </div>
            <textarea class="form-control" aria-label="With textarea"></textarea>
          </div>
          <hr>
            <div class="input-group">
              <div class="input-group-prepend">
                <span class="input-group-text">Input Text</span>
              </div>
              <textarea class="form-control" aria-label="With textarea"></textarea>
            </div>
              </blockquote>
            </div>
          </div>

        <!-- jQuery (부트스트랩의 자바스크립트 플러그인을 위해 필요합니다) -->
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
      </body>
    </html>
    ''' 

@app.route('/message/<message>')
def user(message):
    return f'{message}'

if __name__ == '__main__':
    app.run()