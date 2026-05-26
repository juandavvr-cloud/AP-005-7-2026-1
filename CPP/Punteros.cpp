#include <iostream>
using namespace std;

// 1FUNCIONES

// duplicar valor usando puntero
void duplicar(int *p) {
    if (p != NULL) {
        *p = (*p) * 2;
    }
}

// intercambiar valores
void intercambiar(int *a, int *b) {
    if (a == NULL || b == NULL) return;

    int temp = *a;
    *a = *b;
    *b = temp;
}

// mostrar vector
void mostrarVector(int *p, int n) {
    if (p == NULL) return;

    for (int i = 0; i < n; i++) {
        cout << *(p + i) << " ";
    }
    cout << endl;
}

// incrementar vector
void incrementarVector(int *p, int n) {
    if (p == NULL) return;

    for (int i = 0; i < n; i++) {
        *(p + i) = *(p + i) + 1;
    }
}

// multiples resultados
void analizar(int v[], int n, int *suma, int *mayor, int *menor) {
    *suma = 0;
    *mayor = v[0];
    *menor = v[0];

    for (int i = 0; i < n; i++) {
        *suma += v[i];

        if (v[i] > *mayor) *mayor = v[i];
        if (v[i] < *menor) *menor = v[i];
    }
}

// ===== MAIN =====

int main() {
    int x = 10;
    int y = 20;
    int v[3] = {5, 6, 7};

    int opcion;

    do {
        cout << "\n===== MENU DE PUNTEROS =====\n";
        cout << "1. Mostrar x, direccion y puntero\n";
        cout << "2. Duplicar x con puntero\n";
        cout << "3. Intercambiar x y y\n";
        cout << "4. Mostrar vector\n";
        cout << "5. Incrementar vector\n";
        cout << "6. Analizar vector (suma, mayor, menor)\n";
        cout << "7. Memoria dinamica\n";
        cout << "0. Salir\n";
        cout << "Opcion: ";
        cin >> opcion;

        switch (opcion) {

        case 1: {
            int *p = &x;
            cout << "x = " << x << endl;
            cout << "&x = " << &x << endl;
            cout << "p = " << p << endl;
            cout << "*p = " << *p << endl;
            break;
        }

        case 2:
            cout << "Antes: " << x << endl;
            duplicar(&x);
            cout << "Despues: " << x << endl;
            break;

        case 3:
            cout << "Antes: x=" << x << " y=" << y << endl;
            intercambiar(&x, &y);
            cout << "Despues: x=" << x << " y=" << y << endl;
            break;

        case 4:
            cout << "Vector: ";
            mostrarVector(v, 3);
            break;

        case 5:
            cout << "Antes: ";
            mostrarVector(v, 3);
            incrementarVector(v, 3);
            cout << "Despues: ";
            mostrarVector(v, 3);
            break;

        case 6: {
            int suma, mayor, menor;
            analizar(v, 3, &suma, &mayor, &menor);

            cout << "Suma: " << suma << endl;
            cout << "Mayor: " << mayor << endl;
            cout << "Menor: " << menor << endl;
            break;
        }

        case 7: {
            int n;
            cout << "Tamano del arreglo: ";
            cin >> n;

            int *dyn = new int[n];

            for (int i = 0; i < n; i++) {
                cout << "Ingrese dato " << i << ": ";
                cin >> dyn[i];
            }

            cout << "Datos: ";
            for (int i = 0; i < n; i++) {
                cout << dyn[i] << " ";
            }
            cout << endl;

            delete[] dyn;
            dyn = NULL;

            break;
        }

        case 0:
            cout << "Fin\n";
            break;

        default:
            cout << "Opcion invalida\n";
        }

    } while (opcion != 0);

    return 0;
}