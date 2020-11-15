import sys 
from PyQt5.QtWidgets import  *

Calculador = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Cáculo do IMC - Índice de Massa Corporal')
layout = QVBoxLayout()
altura = QLineEdit()
peso = QLineEdit()
nome = QLineEdit()
endereco = QLineEdit()
label = QLabel('Altura (cm)')
label2 = QLabel('Peso (Kg)')
label3 = QLabel('Nome do Paciente:')
label4 = QLabel('Endereço Completo: ')
button = QPushButton('Calcular')
button.setStyleSheet('QPushButton {background-color: #028fff}')
imc=QLineEdit()

layout.addWidget(label3)
layout.addWidget(nome)
layout.addWidget(label4)
layout.addWidget(endereco)
layout.addWidget(label)
layout.addWidget(altura)
layout.addWidget(label2)
layout.addWidget(peso)
layout.addWidget(button)
layout.addWidget(QLabel('Resultado'))
layout.addWidget(imc)


def CalcularIMC():
    h=float(altura.text())
    p=float(peso.text())
    r= p / (h ** 2)
    if r < 17:
        imc.setText('O IMC do paciente é de {:.1f} ele está MUITO ABAIXO DO PESO'.format(r))
    elif 17 <= r < 18.49:
        imc.setText('O IMC desse paciente é de {:.1f} ele está ABAIXO DO PESO'.format(r))
    elif 18.50 <= r < 24.99:
        imc.setText('O IMC desse paciente é de {:.1f} ele está com o PESO NORMAL'.format(r))
    elif 25 <= r < 30:
        imc.setText('O IMC desse paciente é de {:.1f} ele está ACIMA DO PESO'.format(r))
    elif 30 <= r < 34.99:
        imc.setText('O IMC desse paciente é de {:.1f} ele está em OBESIDADE I'.format(r))
    elif 35 <= r < 39.99:
        imc.setText('O IMC desse paciente é de {:.1f} ele está em OBESIDADE II (severa)'.format(r))
    else:
        imc.setText('O IMC desse paciente é de {:.1f} ele está em OBESIDADE III (mórbida)'.format(r))

    

button.clicked.connect(CalcularIMC)

window.setLayout(layout)
window.show()
Calculador.exec()