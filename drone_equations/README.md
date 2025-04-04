## Controlador drone
### comandos bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt


As Equações de movimento para o movimento nos três eixos é dado por :

$$\ddot{x} = (\cos\phi \sin\theta \cos\psi + \sin\phi \sin\psi) \frac{1}{m} U_1$$
$$\ddot{y} = (\cos\phi \sin\theta \sin\psi - \sin\phi \cos\psi) \frac{1}{m} U_1,$$
$$\ddot{z} = -g + (\cos\phi \cos\theta) \frac{1}{m} U_1,$$
Sendo $U_1$, a tração fornecida pelo conjunto de motores.
Como queremos apenas controlar a altitude  tomamos a equação no eixo Z


$$\ddot{z} = -g + \frac{\cos\phi \cdot \cos\theta}{m} U_1$$

A equação acima não é linear e demandaria um controlador mais sofisticado , porém podemos linearizar a equação, e obter uma equação simples.
Assumindo pequenas oscilações , podemos simplificar para:

$$\ddot{z} = -g + \frac{U_1}{m}$$

$$s^2 Z(s) = -g + \frac{U_1(s)}{m}
$$

A função de transferência de altitude é:

$$G_z(s) = \frac{Z(s)}{U_1(s)} = \frac{1}{m s^2}$$
