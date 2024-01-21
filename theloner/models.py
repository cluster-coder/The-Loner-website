from django.db import models

#Information for option
tags=[
    ('div','div'),
    ('pre','pre'),
    ('img','img'),
    ('pre','pre'),
    ('p','p'),
    ('h1','h1'),
    ('h2','h2'),
    ('h3','h3'),
    ('h4','h4'),
    ('h5','h5'),
    ('h6','h6'),
]

baseElements=[
    (0, 'header'),
    (1, 'wolf'),
    (2, 'choices'),
    (3, 'tellstory'),
    (4, 'beyond'),
]

# Create your models here.


class SecretUrl(models.Model):
    secretWord=models.CharField(max_length=100)
    additionalCss=models.CharField(max_length=800, blank=True)
    cssIsInternalLink=models.BooleanField(default=False)

    def __str__(self):
        return self.secretWord



class choices(models.Model):
    bodyClass=models.CharField(max_length=2000, blank=True)
    wolfClass=models.CharField(max_length=2000, blank=True)
    wolfText=models.CharField(max_length=2000)

    realwolfClass=models.CharField(max_length=2000, blank=True)

    iconClass=models.CharField(max_length=2000, blank=True)
    iconSrc=models.CharField(max_length=800, blank=True)
    iconIsInternalLink=models.BooleanField(default=False)

    headerClass=models.CharField(max_length=2000, blank=True)
    headerCssUrl=models.CharField(max_length=800, blank=True)
    headerIsInternalLink=models.BooleanField(default=False)

    choicesClass=models.CharField(max_length=2000, blank=True)
    timeoptionClass=models.CharField(max_length=2000, blank=True)
    timeoptionText=models.CharField(max_length=2000, blank=True)
    timeoptionAnimation=models.CharField(max_length=2000, blank=True)

    tellstoryClass=models.CharField(max_length=2000, blank=True)
    tellstoryText=models.TextField(blank=True)

    urlBearer=models.ForeignKey(
        SecretUrl, on_delete=models.CASCADE)
    position=models.PositiveSmallIntegerField()
    '''
    #parando pra pensar, choices de uma mesma url
    #podem conter o mesmo wolf, mas conteudos diferentes
    #não conseguiria diferenciar between choices.
    def __str__(self):
        return self.wolfText
    '''
    def __str__(self):
        return self.wolfText + str(self.position)


class additionalHtml(models.Model):
    pages_adding_me=models.ManyToManyField(SecretUrl, blank=True)
    options_adding_me=models.ManyToManyField(choices, blank=True)
    tagType=models.CharField(max_length=100, choices=tags)
    tagClasses=models.CharField(max_length=2000, blank=True)
    contentInside=models.TextField(blank=True)
    insertBefore=models.IntegerField(choices=baseElements)

    def Pages_its_used_in(self):
        pages=[]
        for page in self.pages_adding_me.all():
            pages.append(page)
        return pages

    def options_its_used_in(self):
        options=[]
        for option in self.options_adding_me.all():
            options.append(option)
        return options

    def __str__(self):
        return f'{self.tagType} before {baseElements[self.insertBefore][1]}'