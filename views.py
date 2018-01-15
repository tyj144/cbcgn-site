from django.shortcuts import render, get_object_or_404
from content.models import Event, Category, Sermon
from content.tblscraper import scrape

import feedparser, time

# Create your views here.
def index(request):
	return render(request, 'index.html', {'events': Event.objects.all()[:5]})

def home(request):
	return render(request, 'home.html', )

def about(request):
	return render(request, 'about.html')

def sermons(request):
	'''pulls sermons from the old sharepoint site and displays them'''
	
	
	sermons = scrape(url="https://cbcgn-public.sharepoint.com/sunday-sermons1", 
				headers=['Date', 'Speaker', 'Title'], links=True, prefix='https://cbcgn-public.sharepoint.com')

	return render(request, 'sermons.html', { 'recent_sermon': sermons[0], 'sermons': sermons[1:10]})


#	# get sermons from database instead of scraping
# 	return render(request, 'sermons.html', { 'sermons': Sermon.objects.all() })

def youth(request):
	url = 'https://groups.google.com/forum/feed/cbcgn-youth-group/topics/rss.xml?num=50'
	# strips last 10 posts from RSS feed
	posts = feedparser.parse(url).entries[:10]
	# formats the date and time of each post
	for post in posts:
		post['published'] = time.strftime('%B %-d', post.published_parsed)
	# sends all 10 posts to be rendered in the webpage
	return render(request, 'youth.html', {'posts':posts})

# Unused views
# def view_event(request, slug):
# 	return render(request, 'view_event.html', { 'event': get_object_or_404(Event, slug=slug) })

# def view_category(request, slug):
# 	category = get_object_or_404(Category, slug=slug)

# 	return render(request, 'view_category.html', { 
# 		'category': category,
# 		'events': Event.objects.filter(category=category)[:5],
# 	})