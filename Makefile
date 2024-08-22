
all: top.pdf split

extra: margin_maximization.tex

# linear_classifiers.tex perceptron.tex logistic_regression.tex

# top.pdf: top.tex \
# 	intro.tex \
# 	regression.tex \
# 	gradient_descent.tex \
# 	classification.tex \
# 	feature_representation.tex \
# 	clustering.tex \
# 	neural_networks.tex \
# 	neural_networks_2.tex \
# 	autoencoders.tex \
# 	convolutional_neural_networks.tex \
# 	rnn.tex \
# 	transformers.tex \
# 	mdp.tex \
# 	reinforcement_learning.tex \
# 	non_parametric.tex \
# 	matrix_derivative.tex \
# 	nutshell.tex \
# 	macros.tex

top.pdf:
	pdflatex top

split:	top.pdf
	python3 make_chapter_pdfs.py
	touch split
	cp top.pdf chapter_pdfs/6_390_lecture_notes_fall24.pdf

to_catsoop: top.pdf split
	cp chapter_pdfs/*.pdf ../web/__STATIC__/LectureNotes/
