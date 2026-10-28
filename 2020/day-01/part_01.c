#include <stdio.h>
#include <stdlib.h>

int main() {

  FILE *myFile;
  myFile = fopen("sample.txt", "r");
  char line[128];

  int numberArray[16];
  int i;

  if (myFile == NULL) {
    printf("Error Reading File\n");
    exit(0);
  }

  while (fgets(line, sizeof(line), myFile) != NULL) {
    int a;
    if (sscanf(line, "%d", &a) == 1) {
      printf("%d\n", a);
    };
  };

  // for (i = 0; i < 16; i++) {
  //   fscanf(myFile, "%d,", &numberArray[i]);
  // }
  //
  // for (i = 0; i < 16; i++) {
  //   printf("Number is: %d\n\n", numberArray[i]);
  // }
  fclose(myFile);
  return 0;
}
