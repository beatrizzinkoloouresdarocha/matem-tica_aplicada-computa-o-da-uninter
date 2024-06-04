//1)exemplo do que é:União de Conjuntos
//A união de dois conjuntos contém todos os elementos de ambos os conjuntos sem duplicatas.

function union(setA, setB) {
    return new Set([...setA, ...setB]);
}

// Exemplo de uso
const setA = new Set([1, 2, 3]);
const setB = new Set([3, 4, 5]);
const unionSet = union(setA, setB);
console.log(unionSet); // Output: Set { 1, 2, 3, 4, 5 }

//2)exemplo:Vetores (Arrays)

let vetor = [1, 2, 3, 4, 5];
console.log(vetor); // Output: [1, 2, 3, 4, 5]

//3)exemplo:Funções Simples

function saudacao(nome) {
    return `Olá, ${nome}!`;
}

// Exemplo de uso
console.log(saudacao("João")); // Output: Olá, João!

//4)exemplo:Avaliação de Polinômios

function avaliarPolinomio(coeficientes, x) {
    return coeficientes.reduce((acumulador, coeficiente, indice) => acumulador + coeficiente * Math.pow(x, indice), 0);
}

// Exemplo de uso
const polinomio = [5, 0, 3, 2]; // 2x^3 + 3x^2 + 0x + 5
const x = 2;
console.log(avaliarPolinomio(polinomio, x)); // Output: 33

//5)exemplo:Noções aritméticas básicas envolvem operações fundamentais como adição, subtração, 
//multiplicação e divisão. Vamos ver como essas operações podem ser realizadas e alguns conceitos 
//relacionados em JavaScript.

//Adição

const a = 5;
const b = 3;
const soma = a + b;
console.log(soma); // Output: 8

//Gerar Números Aleatórios

const aleatorio = Math.random();
console.log(aleatorio); // Output: um número aleatório entre 0 e 1

// Número aleatório entre 1 e 10
const aleatorioEntre1e10 = Math.floor(Math.random() * 10) + 1;
console.log(aleatorioEntre1e10);
