from flask import Flask, render_template, request, flash, redirect, url_for
app = Flask(__name__)


@app.route('/escape', methods=["GET", "POST"])
def index(): 
	print("request " + str(request))
	if request.method == "GET":
		return render_template('index.html', ButtonPressed = 0)
	else: # if you press the button with the correct puzzle, will bring you to another page (loc2)
		# return redirect("loc2", code=302)
		# send text message to person's phone and if code is correct, redirect to the next page. 
		return redirect(url_for('loc2', solvedpuzzle='true'))

@app.route('/loc2')
def loc2():
	print("request2 " + str(request.url))
	if request.method == "GET":
		# if no query that says solved puzzle = true, redirect back to start page with an alert 
		if "solvedpuzzle=true" in request.url:
			return render_template('button.html')
		else:
			return redirect('escape')
	return render_template('button.html')

if __name__ == '__main__':
    app.run()


