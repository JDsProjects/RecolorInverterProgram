#define OLC_PGE_APPLICATION
#include <iostream>
#include <string>
#include <cstdlib>
#include <sstream>
#include "./Headers/Split.h"
#include "Headers/Windows.h"
#include "Headers/FileLoading.h"
#include "Headers/Hex_to_int.h"
#include "Headers/olcPixelGameEngine.h"
#include "Headers/Structs/Body.h"
//using namespace std;
bool colorCodeActive = 0;
std::string colorModes[2] = {"Empty","Loaded"};


std::vector<bodyPart> bodyParts;
void loadBody() {
    bodyParts.clear();
    std::string fileName = sb::openfn("Choose a Color Code To Open");
    std::vector<std::string> lines = LoadFile(fileName);
    for (int lineNum = 0; lineNum + 1 < lines.size(); lineNum += 2) {
        bodyPart tmpBodypart(lines[lineNum], lines[lineNum + 1]);
        // tmpBodypart.partColor.invert();
         //tmpBodypart.printColorCode();
        bodyParts.push_back(tmpBodypart);
    }
}
void invertAll(olc::PixelGameEngine* pge) {
    for (auto colour : bodyParts) {
        colour.partColor.invert();
        MessageBox(NULL, L"Color Code Inverted!", L"JDJG Color Code Inverter", NULL);
    }
}
class JDJG : public olc::PixelGameEngine
{
public:
    JDJG()
    {
        sAppName = "JDJG Color Code Inverter";
    }

public:
    void init() {
        //background
        for (unsigned int i = 0; i < 440 / 10; i++)
            for (unsigned int i1 = 0; i1 < 300 / 10; i1++)
                this->FillRect(i * 10, i1 * 10, 10, 10, olc::Pixel(rand() % 255, rand() % 255, rand() % 255));
        //Color Code status
        this->FillRect(14, 20, 410, 25, olc::WHITE);
        this->DrawRect(14, 20, 410, 25, olc::BLACK);
        this->DrawString({ 18,24 }, ("Color Code Status: " + colorModes[colorCodeActive]), olc::BLACK, 2);
        //Import Button
        this->FillRect(20, 60, 125, 50, olc::Pixel(255, 255, 255));
        this->DrawRect(20, 60, 125, 50, olc::Pixel(0, 0, 0));
        this->DrawString({ 20 + 15,60 + 15 }, "Import", olc::BLACK, 2);
        //Export Button
        this->FillRect(275, 60, 125, 50, olc::Pixel(255, 255, 255));
        this->DrawRect(275, 60, 125, 50, olc::Pixel(0, 0, 0));
        this->DrawString({ 275 + 15,60 + 15 }, "Export", olc::BLACK, 2);
        //Invert Button
        this->FillRect(150, 150, 125, 50, olc::Pixel(255, 255, 255));
        this->DrawRect(150, 150, 125, 50, olc::Pixel(0, 0, 0));
        this->DrawString({ 150 + 15,150 + 15 }, "Invert", olc::BLACK, 2);

    }
    bool OnUserCreate() override
    {
        init();
        return true;
    }

    bool OnUserUpdate(float fElapsedTime) override
    {
        if (GetMouse(0).bPressed) {
            olc::vi2d ms = { GetMouseX(),GetMouseY() };
            if (ms.y < 60 + 50 && ms.y >60) {
                if (ms.x < 20 + 125 && ms.x > 20) {
                    //Import
                    loadBody();
                    colorCodeActive = 1;
                    init();
                }
                if (ms.x < 275 + 125 && ms.x > 275) {
                    //Export
                    for (auto part : bodyParts) {
                        part.printColorCode();
                    }
                    std::cout << "\n";
                }
            }
            if (ms.y < 150 + 50 && ms.y >150) {
                if (ms.x > 150 && ms.x < 150 + 125) {
                   //Invert
                    for (int i = 0; i < bodyParts.size();i++) {
                        bodyParts[i].partColor.invert();
                    }
                    init();
                }
            }
        }
        return true;
    }
};

int main()
{
    JDJG  colorCodeInverter;
    if (colorCodeInverter.Construct(440, 300, 1, 1,0,1))
        colorCodeInverter.Start();
    return 0;
}
//COMPLETED CODE

/*
  r = int(color_section[0:2], 16)
  g = int(color_section[2:4], 16)
  b = int(color_section2[0:2], 16)
  r = 0xFF - r
  g = 0xFF - g
  b = 0xFF - b
*/

//STILL NEEDS TO BE CONVERTED

/*


*/




/*
Inverted_color_code = []

Inverted_color_code_inverted = []

times_ran_1 = 0
lines=complete_color_code.split("\n")

while times_ran_1 < len(lines):

  if '' == lines[times_ran_1]:

    times_ran_1 = times_ran_1+1

    Inverted_color_code.append('')

    Inverted_color_code_inverted.append('')

  if not '' == lines[times_ran_1]:

    break

x = int(times_ran_1)

color_counter = 0
times_ran_program_1 = 0

while x+1 < len(lines):

  color_value = lines[x]

  color_value2 = lines[x+1]

  colored_bit=color_value.split(" ")

  colored_bit2 = color_value2.split(" ")

  color_code_front = colored_bit[0]

  color_code_front2 = colored_bit2[0]

  color_section = colored_bit[1]

  color_section2 = colored_bit2[1]
  r = int(color_section[0:2], 16)
  g = int(color_section[2:4], 16)
  b = int(color_section2[0:2], 16)
  r = 0xFF - r
  g = 0xFF - g
  b = 0xFF - b
  bits_used998 = f"{r:0{2}x}{g:0{2}x}{b:0{2}x}"

  first_color_line =  bits_used998[0:4].upper()

  second_color_line = bits_used998[4:6].upper()

  color_code_needed = color_code_front+" "+first_color_line

  color_code_needed_2 = color_code_front2+" "+second_color_line+color_section2[2:4]

  Inverted_color_code.append(color_code_needed)

  Inverted_color_code.append(color_code_needed_2)

  x = x +2

  color_counter = color_counter + 1

  times_ran_program_1 = times_ran_program_1 + 1

times_ran_1 = 0

while times_ran_1 < len(Inverted_color_code):

  if '' == Inverted_color_code[times_ran_1]:

    times_ran_1 = times_ran_1+1

  if not '' == Inverted_color_code[times_ran_1]:

    break

z = int(times_ran_1)

while z+1 < len(Inverted_color_code):

  color_value = Inverted_color_code[z]

  color_value2 = Inverted_color_code[z+1]

  colored_bit=color_value.split(" ")

  colored_bit2 = color_value2.split(" ")

  color_code_front = colored_bit[0]

  color_code_front2 = colored_bit2[0]

  color_section = colored_bit[1]

  color_section2 = colored_bit2[1]
  r = int(color_section[0:2], 16)
  g = int(color_section[2:4], 16)
  b = int(color_section2[0:2], 16)
  r = 0xFF - r
  g = 0xFF - g
  b = 0xFF - b
  bits_used998 = f"{r:0{2}x}{g:0{2}x}{b:0{2}x}"
  first_color_line =  bits_used998[0:4].upper()

  second_color_line = bits_used998[4:6].upper()
  color_code_needed_2 = color_code_front+" "+first_color_line

  color_code_needed_2 = color_code_front2+" "+second_color_line+color_section2[2:4]
  Inverted_color_code_inverted.append(color_code_needed)

  Inverted_color_code_inverted.append(color_code_needed_2)
  z = z +2

  color_counter2 = color_counter2 + 1


if Inverted_color_code_inverted == lines:

  pass

  if not Inverted_color_code_inverted == lines:

    pass

while j < len(Inverted_color_code):

  test_string99 = test_string99+(Inverted_color_code[j]+"\n")


  j = j + 1

*/