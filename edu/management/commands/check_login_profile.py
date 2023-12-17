from django_celery_beat.models import PeriodicTask, IntervalSchedule

def set_schedule(every=None, period=None, name=None, task=None):
	if not (every and period and name and task):
		every, period, name, task = 1, IntervalSchedule.MONTH, 'Check login profile', 'user.tasks.block_user'
	schedule, created = IntervalSchedule.objects.get_or_create(
	     every=every,
	     period=period # IntervalSchedule.SECONDS,
	 )
	PeriodicTask.objects.create(
	     interval=schedule,
	     name=name #'Add numbers',
	     task=task #'my_app.tasks.add_numbers',
	     args=json.dumps(['arg1', 'arg2']),
	     kwargs=json.dumps({
	        'be_careful': True,
	     }),
	     expires=datetime.utcnow() + timedelta(seconds=30)
	 )