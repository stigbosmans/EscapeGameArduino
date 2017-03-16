const int YELLOW=0;
const int GREEN=1;
const int ORANGE=3;
const int GREY=5;
int count=0;
int cablesConnected[4]={0,0,0,0};

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  //Yellow:0, Green:1, Orange:2, Grey:3
  
  set_state(cablesConnected,YELLOW);
  set_state(cablesConnected,GREEN);
  set_state(cablesConnected,ORANGE);
  set_state(cablesConnected,GREY);
  print_state(cablesConnected);
  delay(100);
}

void print_state(int connected[4]){
  Serial.println(String(connected[0])+String(connected[1])+String(connected[2])+String(connected[3])+";");
}

void set_state(int connected[4],int color){
  if(is_low(color) && connected[get_color_index(color)]==0){
    count++;
    connected[get_color_index(color)]=count;
  }
}

int get_color_index(int color){
  if(color==0){
    return 0;
  }else if(color==1){
    return 1;
  }else if(color==3){
    return 2;
  }else if(color==5){
    return 3;
  }else{
    return 0;
  }
}

bool is_low(int color){
  return analogRead(color)<1000;
}

