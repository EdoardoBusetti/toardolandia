from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from my_scripts.happy_functions import make_word
from toardolandia.extensions import db





class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer, primary_key=True)
    customer = db.Column(db.String(200), unique=True)
    dealer = db.Column(db.String(200))
    rating = db.Column(db.Integer)
    comments = db.Column(db.Text())
    def __init__(self, customer, dealer, rating, comments):
        self.customer = customer
        self.dealer = dealer
        self.rating = rating
        self.comments = comments

class EmojiLetter(db.Model):
    __tablename__ = 'emoji_letter'
    id = db.Column(db.Integer, primary_key=True)
    user_ip_address = db.Column(db.String(100))
    timestamp_utc = db.Column(db.DateTime)
    emojify_text = db.Column(db.Text())
    background_emoji = db.Column(db.String(10))
    characters_emoji = db.Column(db.String(10))
    def __init__(self, user_ip_address, timestamp_utc, emojify_text, background_emoji, characters_emoji):
        self.user_ip_address = user_ip_address
        self.timestamp_utc = timestamp_utc
        self.emojify_text = emojify_text
        self.background_emoji = background_emoji
        self.characters_emoji = characters_emoji



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        customer = request.form['customer']
        dealer = request.form['dealer']
        rating = request.form['rating']
        comments = request.form['comments']
        if customer == '' or dealer == '':
            return render_template('index.html', message='Please enter required fields')
        if db.session.query(Feedback).filter(Feedback.customer == customer).count() == 0:
            data = Feedback(customer, dealer, rating, comments)
            db.session.add(data)
            db.session.commit()
            return render_template('success.html')
        return render_template('index.html', message='You have already submitted feedback')


@app.route('/emoji_lettermaker', methods=['POST','GET'])
def emoji_lettermaker():
    if request.method == 'POST':
        message = None
        emojify_text = request.form['emojify_text']
        background_emoji = request.form['background_emoji']
        characters_emoji = request.form['characters_emoji']
        timestamp_utc = datetime.utcnow()
        user_ip_address = request.access_route[-1] 
        if len(emojify_text) > 200:
            if (len(background_emoji) > 5) or (len(characters_emoji) > 5):
                data = EmojiLetter(user_ip_address, timestamp_utc, emojify_text[:200], background_emoji[:5], characters_emoji[:5])
                db.session.add(data)
                db.session.commit()
                return render_template('emoji_lettermaker.html', message="Max Char Size is 200 - Also, please enter just one emoji per field")
            else:
                data = EmojiLetter(user_ip_address, timestamp_utc, emojify_text[:200], background_emoji, characters_emoji)
                db.session.add(data)
                db.session.commit()    
                return render_template('emoji_lettermaker.html', message="Max Char Size is 200")

        if (len(background_emoji) > 5) or (len(characters_emoji) > 5):
            data = EmojiLetter(user_ip_address, timestamp_utc, emojify_text, background_emoji[:5], characters_emoji[:5])
            db.session.add(data)
            db.session.commit() 
            return render_template('emoji_lettermaker.html', message="Please enter just one emoji per field")

        data = EmojiLetter(user_ip_address, timestamp_utc, emojify_text, background_emoji, characters_emoji)
        db.session.add(data)
        db.session.commit()       
        try:
            background_emoji = background_emoji.replace(" ","")
        except:
            background_emoji = ""
        try:
            characters_emoji = characters_emoji.replace(" ","")
        except:
            characters_emoji = ""
        if (len(background_emoji) > 2) or (len(characters_emoji) > 2) or (len(background_emoji) < 1) or (len(characters_emoji) < 1):
            background_emoji = "🔥"
            characters_emoji = "💧"
            message = "NOTE: Used Default Values.\n \n"
        try:
            emojified_string = make_word(input_str = emojify_text, background_emoji=background_emoji, characters_emoji=characters_emoji)
        except:
            return render_template('emoji_lettermaker.html', message='Input should be a str with no numbers or special chars')

        return render_template('emoji_lettermaker.html', message = message,emojfied_str = emojified_string)
    else:
        return render_template('emoji_lettermaker.html')



@app.route('/emoji_lettermaker2', methods=['POST','GET'])
def emoji_lettermaker2():
    if request.method == 'POST':
        message = None
        emojify_text = request.form['emojify_text']
        background_emoji = request.form['background_emoji']
        characters_emoji = request.form['characters_emoji']
        timestamp_utc = datetime.utcnow()
        user_ip_address = request.access_route[-1] 
        if len(emojify_text) > 200:
            if (len(background_emoji) > 6) or (len(characters_emoji) > 6):
                data = EmojiLetter(user_ip_address, timestamp_utc, emojify_text[:200], background_emoji[:5], characters_emoji[:5])
                db.session.add(data)
                db.session.commit()
                return render_template('emoji_lettermaker2.html', message="Max Char Size is 200 - Also, please enter just one emoji per field")
            else:
                data = EmojiLetter(user_ip_address, timestamp_utc, emojify_text[:200], background_emoji, characters_emoji)
                db.session.add(data)
                db.session.commit()    
                return render_template('emoji_lettermaker2.html', message="Max Char Size is 200")

        if (len(background_emoji) > 5) or (len(characters_emoji) > 5):
            data = EmojiLetter(user_ip_address, timestamp_utc, emojify_text, background_emoji[:5], characters_emoji[:5])
            db.session.add(data)
            db.session.commit() 
            return render_template('emoji_lettermaker2.html', message="Please enter just one emoji per field")

        data = EmojiLetter(user_ip_address, timestamp_utc, emojify_text, background_emoji, characters_emoji)
        db.session.add(data)
        db.session.commit()       
        try:
            background_emoji = background_emoji.replace(" ","")
        except:
            background_emoji = ""
        try:
            characters_emoji = characters_emoji.replace(" ","")
        except:
            characters_emoji = ""
        if (len(background_emoji) > 2) or (len(background_emoji) < 1):
            background_emoji = "⬜"
            message = "NOTE: Used default values for background emoji.\n \n"
        elif (len(characters_emoji) > 2)  or (len(characters_emoji) < 1):
            characters_emoji = "⬜"
            message = "NOTE: Used default values for characters emoji.\n \n"
        try:
            emojified_string = make_word(input_str = emojify_text, background_emoji=background_emoji, characters_emoji=characters_emoji)
        except:
            return render_template('emoji_lettermaker2.html', message='Input should be a str with no numbers or special chars')

        return render_template('emoji_lettermaker2.html', message = message,emojfied_str = emojified_string)
    else:
        return render_template('emoji_lettermaker2.html')


if __name__ == '__main__':
    app.run()