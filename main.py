import instaloader
from flask import Flask, request

app = Flask(__name__)
loader = instaloader.Instaloader()

@app.route('/perfil_instagram')
def obter_posts_instagram():
    profile_name = request.args.get('perfil')  # Obtém o parâmetro 'perfil' da URL

    if not profile_name:
        return "Especifique o nome do perfil na URL.", 400  # Retorna erro se não for fornecido um nome de perfil

    try:
        profile = instaloader.Profile.from_username(loader.context, profile_name)
        posts = profile.get_posts()
        post_urls = [f"https://www.instagram.com/p/{post.shortcode}/" for post in posts]
        return "\n".join(post_urls), 200  # Retorna as URLs dos posts

    except Exception as e:
        return f"Erro ao obter os posts do perfil: {str(e)}", 500  # Retorna erro se ocorrer algum problema

if __name__ == '__main__':
    app.run(debug=True)
