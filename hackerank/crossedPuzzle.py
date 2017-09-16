class Solution():

    def __init__(self, matrix, word_init_dic, word_lenght_dic):
        self.matrix = matrix
        self.word_init_dic = word_init_dic
        self.word_lenght_dic = word_lenght_dic

    def crosswordPuzzleSolver(self, matrix, word_init_dic, word_length_dic):
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] != "+":



if __name__ == '__main__':
    input_matrix = "+-++++++++;+-++++++++;+-------++;+-++++++++;+-++++++++;+------+++;+-+++-++++;+++++-++++;+++++-++++;++++++++++"
    matrix = [ [c for c in line] for line in input_matrix.split(";")]
    input_words = "AGRA;NORWAY;ENGLAND;GWALIOR"
    words = input_words.split(";")
