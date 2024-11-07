def feet_to_steps(user_feet):
   return (user_feet/2.5)

if __name__ == '__main__':
    user_feet = float(input())
    print(f'{feet_to_steps(user_feet):.0f}')
    feet_to_steps(5280)