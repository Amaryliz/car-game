command = ''
started = False
while True:
   command =  input('> ').lower()
   if command == 'start':
       if started:
           print('car is already started ')
       else:
           started = True
           print('the car started')
   elif command == 'stop':
       if not started:
           print('car is already stopped')
       else:
           stop = True
           print('the car stopped')
   elif command == 'slow':
       print('the car has slowed down')
   elif command == 'help':
       print('''
start - starts the car
stop - car stops
slow - car will slow down
quit - to quit game'''
       )
   elif command =='quit':
       break
   else:
       print('Sorry i don\'t understand')




