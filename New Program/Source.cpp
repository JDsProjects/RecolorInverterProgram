#define OLC_PGE_APPLICATION
#include "Headers/olcPixelGameEngine.h"
#include "Headers/Sprite.h"
class Example : public olc::PixelGameEngine
{
public:
	Example()
	{
		sAppName = "";
	}

public:
	bool OnUserCreate() override
	{
		return true;
	}

	bool OnUserUpdate(float fElapsedTime) override
	{
		return true;
	}
};
int main()
{
	Example demo;
	if (demo.Construct(300, 300, 1, 1))
		demo.Start();
	return 0;
}
