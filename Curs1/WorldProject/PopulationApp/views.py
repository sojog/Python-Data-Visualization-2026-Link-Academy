from django.shortcuts import render
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import matplotlib
import pandas as pd
# Create your views here.

matplotlib.use("svg")

countries = ['Bangladesh', 'Brazil', 'China', 'India', 'Indonesia', 'Mexico', 'Nigeria', 'Pakistan', 'Russia', 'United States']
population = [170, 213, 1411, 1378, 271, 126, 211, 225, 146, 331]
df = pd.DataFrame({"countries":countries, "population":population})

def get_countries_population(filter_countries):
	filtered_df =  df[df["countries"].isin(filter_countries)]
	return list(filtered_df["countries"]), list(filtered_df["population"])


def all_countries_view(request):
	context = {}
	return render(request, 'all_countries.html', context)



def create_image(by_countries):
	filtered_countries, filtered_population = get_countries_population(by_countries)
	print("Image to create:", filtered_countries, filtered_population)
	plt.pie(filtered_population, labels=filtered_countries, autopct="%1.2f%%");

	buffer = BytesIO()
	plt.savefig(buffer, format="png")
	buffer.seek(0)
	image_png = buffer.getvalue()
	buffer.close()

	plt.close()
	return base64.b64encode(image_png).decode("utf-8")



def choose_countries_view(request):
	if request.method == "POST":
		print("Am primit requestul:", request.POST)
		tarile_primite = request.POST.keys()
		tarile_primite = list(tarile_primite)[1:]
		print("Tarile primite:", tarile_primite, type(tarile_primite))
		new_image = create_image(tarile_primite)
		countries = ['Bangladesh', 'Brazil', 'China', 'India', 'Indonesia', 'Mexico', 'Nigeria', 'Pakistan', 'Russia', 'United States']
		
		context = {'countries': countries, "created_image": new_image}

		return render(request, 'choose_countries.html', context)
		



	else:
		countries = ['Bangladesh', 'Brazil', 'China', 'India', 'Indonesia', 'Mexico', 'Nigeria', 'Pakistan', 'Russia', 'United States']
		context = {'countries': countries}


		return render(request, 'choose_countries.html', context)
	


