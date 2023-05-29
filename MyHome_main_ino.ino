#include "DHT.h" //DHT 헤더파일 불러오기

#define DHTPIN 4        //DHTPIN을 4로 정의
#define DHTTYPE DHT11   //DHTTYPE을 DHT11로 정의
#define LEDPIN 9        //LEDPIN을 9로 정의
#define CDSPIN A0       //CDSPIN을 A0로 정의

DHT dht(DHTPIN, DHTTYPE);   //객체 DHT 생성

void setup() {
  pinMode(LEDPIN, OUTPUT);  //LEDPIN을 OUTPUT으로 설정
  Serial.begin(9600);       //9600보레이트로 시리얼 통신 시작
  dht.begin();              //DHT센서 초기화
}

void loop() {
  float temperature = dht.readTemperature();                //온도를 저장할 float타입 temperature 변수 선언 및 값 대입
  float humidity = dht.readHumidity();                      //습도를 저장할 float타입 humidity 변수 선언 및 값 대입
  int brightness = map(analogRead(CDSPIN), 0, 1024, 1, 10); //밝기를 저장할 int타입 brightness 변수 선언 및 값 대입, map을 활용
  
  if (Serial.available() > 0) {     //만약 시리얼 데이터가 있다면
    char command = Serial.read();   //char 타입 command 변수를 선언 및 값 대입
    if (command == '1') {           //만약 command 값이 1이라면
      digitalWrite(LEDPIN, HIGH);   //LEDPIN을 HIGH로 설정
    } else if (command == '0') {    //만약 command 값이 0이라면
      digitalWrite(LEDPIN, LOW);    //LEDPIN을 LOW로 설정
    } else if (command == 'T') {    //만약 command 값이 T라면
      Serial.println(temperature);  //temperature 값 출력
    } else if (command == 'H') {    //만약 command 값이 H라면
      Serial.println(humidity);     //humidity 값 출력
    } else if (command == 'B') {    //만약 command 값이 B라면
      Serial.println(brightness);   //brightness 값 출력
    }
  }
}