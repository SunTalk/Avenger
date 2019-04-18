
PGraphics pg; 
PFont font;

// void setup(){

	// font = createFont("chris.ttf",1);
	// font = createFont("Holy-Union-2.ttf",1);
	// font = createFont("Ozymandias-2.ttf",1);
	// font = createFont("Royal.ttf",1);
	// font = createFont("Royale.ttf",1);

	// size(600,600); 
	// pg = createGraphics(600, 600); 
	// PImage ice = loadImage("ice.png");
	// PImage fire = loadImage("fire.png");

	// pg.beginDraw(); 

	// pg.image(fire, -50, 140, 700, 320);
	// pg.fill(153,0,255);
	// pg.textFont(font);
	// pg.textSize(100);

	// pg.fill(0);
	// pg.text("T",287,328);
	// pg.fill(102, 0, 204);
	// pg.text("T",285,330);

	// pg.endDraw(); 

	// image(pg, 0, 0);
	// pg.save("iceJJ.png");
	// pg.save("suntalk.png");
// }

void setup(){
	size(1034,650);
	PImage bg = loadImage("LOADING.jpg");
	PImage iceJJ = loadImage("iceJJ.png");
	PImage suntalk = loadImage("suntalk.png");

	image(bg, 0, 0);
	image(iceJJ,700,200,200,200);
	image(suntalk, 100, 120, 350, 350);

	save("LOAD.jpg");
}