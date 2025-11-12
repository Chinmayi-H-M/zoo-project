from django.shortcuts import render

def display_landing(request):
    return render(request, 'landing.html')

tiger = {
    'name': 'Tiger',
    'age': 5,
    'description': 'The tiger is the largest cat species, known for its orange coat with black stripes. It is a powerful predator and an apex carnivore.',
    'image': "https://upload.wikimedia.org/wikipedia/commons/5/56/Tiger.50.jpg",
    'habitat': "Tropical rainforests, grasslands, and mangrove swamps",
    'diet': "Deer, wild boar, and other large mammals",
    'donated_by': "WCS",
    'caretaker': "Mr. Arjun Kumar"
}

monkey = {
    'name': 'Monkey',
    'age': 15,
    'description': 'Monkeys are intelligent primates known for their agility, curiosity, and social behavior. They live in large groups called troops.',
    'image': "https://upload.wikimedia.org/wikipedia/commons/6/6f/Rhesus_macaque_in_Sundarbans.jpg",
    'habitat': "Tropical forests, woodlands, and savannas",
    'diet': "Fruits, leaves, nuts, insects, and small animals",
    'donated_by': "WCS",
    'caretaker': "Mr. Arjun Kumar"
}

elephant = {
    'name': 'Elephant',
    'age': 20,
    'description': 'Elephants are the largest land mammals on Earth, known for their intelligence, strong social bonds, and long trunks.',
    'image': "https://upload.wikimedia.org/wikipedia/commons/3/37/African_Bush_Elephant.jpg",
    'habitat': "Grasslands, forests, and savannas",
    'diet': "Grass, leaves, fruits, and bark",
    'donated_by': "WCS",
    'caretaker': "Mr. Arjun Kumar"
}

lion = {
    'name': 'Lion',
    'age': 15,
    'description': 'The lion is a large carnivorous cat native to Africa and parts of India, known as the "king of the jungle".',
    'image': "https://upload.wikimedia.org/wikipedia/commons/7/73/Lion_waiting_in_Namibia.jpg",
    'habitat': "Grasslands, savannas, and open woodlands",
    'diet': "Deer, antelope, zebra, and buffalo",
    'donated_by': "WCS",
    'caretaker': "Mr. Arjun Kumar"
}

giraffe = {
    'name': 'Giraffe',
    'age': 12,
    'description': 'The giraffe is the tallest land animal, easily recognized by its long neck and spotted coat.',
    'image': "https://upload.wikimedia.org/wikipedia/commons/9/9f/Giraffe_standing.jpg",
    'habitat': "Savannas, grasslands, and open woodlands",
    'diet': "Leaves, flowers, and fruits from tall trees like acacia",
    'donated_by': "WCS",
    'caretaker': "Mr. Arjun Kumar"
}

ostrich = {
    'name': 'Ostrich',
    'age': 8,
    'description': 'The ostrich is the largest and heaviest living bird, native to Africa, and known for its powerful running ability.',
    'image': "https://upload.wikimedia.org/wikipedia/commons/d/d3/Common_ostrich_struthio_camelus.jpg",
    'habitat': "Savannas and desert regions",
    'diet': "Seeds, roots, leaves, and insects",
    'donated_by': "WCS",
    'caretaker': "Mr. Arjun Kumar"
}

peacock = {
    'name': 'Peacock',
    'age': 10,
    'description': 'The peacock is famous for its vibrant tail feathers and beautiful display used to attract mates.',
    'image': "https://upload.wikimedia.org/wikipedia/commons/3/3a/Indian_Peacock.jpg",
    'habitat': "Forests and farmlands",
    'diet': "Seeds, insects, and small reptiles",
    'donated_by': "WCS",
    'caretaker': "Mr. Arjun Kumar"
}

cheetah = {
    'name': 'Cheetah',
    'age': 9,
    'description': 'The cheetah is the fastest land animal, capable of reaching speeds up to 120 km/h in short bursts.',
    'image': "https://upload.wikimedia.org/wikipedia/commons/7/71/Cheetah_Kruger.jpg",
    'habitat': "Grasslands, savannas, and open plains",
    'diet': "Gazelles, impalas, and smaller antelopes",
    'donated_by': "WCS",
    'caretaker': "Mr. Arjun Kumar"
}

zebra = {
    'name': 'Zebra',
    'age': 10,
    'description': 'Zebras are African herbivores known for their distinctive black-and-white stripes and social nature.',
    'image': "https://upload.wikimedia.org/wikipedia/commons/0/0f/Zebra_Botswana_edit02.jpg",
    'habitat': "Grasslands and savannas",
    'diet': "Grasses and leaves",
    'donated_by': "WCS",
    'caretaker': "Mr. Arjun Kumar"
}

python = {
    'name': 'Python',
    'age': 5,
    'description': 'Pythons are non-venomous snakes that kill their prey by constriction and swallow it whole.',
    'image': "https://upload.wikimedia.org/wikipedia/commons/1/1a/Burmese_python_%28Python_bivittatus%29.jpg",
    'habitat': "Tropical forests, grasslands, and swamps",
    'diet': "Small mammals, birds, and reptiles",
    'donated_by': "WCS",
    'caretaker': "Mr. Arjun Kumar"
}

def display_tiger(request):
    return render(request, 'animals.html', context=tiger)
def display_monkey(request):
    return render(request, 'animals.html', context=monkey)
def display_elephant(request):
    return render(request, 'animals.html', context=elephant)
def display_lion(request):
    return render(request, 'animals.html', context=lion)
def display_giraffe(request):
    return render(request, 'animals.html', context=giraffe)
def display_ostrich(request):
    return render(request, 'animals.html', context=ostrich)
def display_peacock(request):
    return render(request, 'animals.html', context=peacock)
def display_cheetah(request):
    return render(request, 'animals.html', context=cheetah)
def display_zebra(request):
    return render(request, 'animals.html', context=zebra)
def display_python(request):
    return render(request, 'animals.html', context=python)


