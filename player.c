/*Get the player details like player number, player name and player run rate. Print the player details.
  Find the highest run rate among the players. */

#include <stdio.h>
struct Player{
    int  no;
    char name[20];
    float run_rate;
};
int main() {
    int n;
    printf("Enter the number of players:");
    scanf("%d",&n);
    struct Player p[n];
    int i;
    for(i=0;i<n;i++){
        printf("Enter the Player number:");
        scanf("%d",&p[i].no);
        printf("Enter the name of the Player:");
        scanf("%s",p[i].name);
        printf("Enter the run rate of the Player:");
        scanf("%f",&p[i].run_rate);
    }
    
    printf("Player Details");
      for(i=0;i<n;i++){
        printf("\nPlayer number: %d",p[i].no);
        printf("\nPlayer name: %s",p[i].name);
        printf("\nPlayer run rate: %.2f",p[i].run_rate);
    }
    
    for(i=1;i<n;i++)
    {
        if (p[0].run_rate<p[i].run_rate)
        {
            p[0].run_rate=p[i].run_rate;
        }
    }
    printf("\nHighest Run Rate: %.2f",p[0].run_rate);
    return 0;
}