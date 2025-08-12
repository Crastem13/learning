var nume_variabila = 10 
// var declara o variabila la nivel global -> oriunde ar fi variabila ea poate fi accesata
let nume_variabila2 = 20
// let declara o variabila la nivel de bloc -> variabila poate fi accesata doar in interiorul blocului in care a fost declarata
const NUME_VAR = 100
// const declara o variabila la nivel global -> oriunde ar fi variabila ea poate fi accesata, dar nu poate fi modificata

10 // INT INTEGER
20.5 // FLOAT FLOATING POINT NUMBER
true // BOOLEAN TRUE
false // BOOLEAN FALSE
"Hello World" // STRING STRING
[1, 2, 3] // ARRAY ARRAY
{ nume: "John"; varsta: 30 } // OBJECT OBJECT
null // NULL NULL
undefined // UNDEFINED UNDEFINED
NaN // NOT A NUMBER NaN


if (nume_variabila > 5 && nume_variabila < 20) {
    console.log("Numele variabilei este mai mare decat 5") // Numele variabilei este mai mare decat 5
} else if (nume_variabila < 5 || nume_variabila > 20) {
    console.log("Numele variabilei este mai mic decat 5")
} else {
    console.log("Numele variabilei este egal cu 5")
}

for (let i = 0; i < 5; i++) {
    console.log(i) // 0 1 2 3 4
}

while (nume_variabila < 20) {
    console.log(nume_variabila) // 10 11 12 13 14 15 16 17 18 19
    nume_variabila++
}

a = 10
a++ // 11
a += 5 // a = a + 5 -> 16
a -= 5 // a = a - 5 -> 11
a *= 5 // a = a * 5 -> 55
a /= 5 // a = a / 5 -> 11
a %= 5 // a = a % 5 -> 1
a **= 5 // a = a ** 5 -> 1

function nume_functie(parametru1, parametru2) {
    return parametru1 + parametru2
}

console.log(nume_functie(10, 20)) // 30
console.log(nume_functie(10, 20, 30)) // 30

async function nume_functie_asincrona(parametru1, parametru2) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve(parametru1 + parametru2)
        }, 1000)
    })
}

await nume_functie_asincrona(10, 20).then((rezultat) => {
    console.log(rezultat) // 30
}).catch((eroare) => {
    console.log(eroare)
})

try {
    let rezultat = await nume_functie_asincrona(10, 20)
    console.log(rezultat) // 30
}catch (eroare) {
    console.log(eroare)
}