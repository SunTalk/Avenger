void setup(){
	size(100,100);
	smooth();
	strokeWeight(5);
	// noStroke();
	// fill(0,255,0); // soldier
	fill(255,0,0); // enemy
	// fill(0,0,0);

	rect(2, 2, 96,96);
	// fill(255,0,0);

	// line(20,50,80,50);
	// line(50,20,50,80);
	// save("enemy_servant.jpg");
	// save("soldier_servant.jpg");

	// ellipse(0,0,102,102);
	// ellipse(100,0,102,102);
	// ellipse(0,100,102,102);
	// ellipse(100,100,102,102);

	// fill(0,0,0);
	// stroke(1);
	// strokeWeight(10);
	// line(0,0,100,100);
	// line(0,0,0,100);
	// line(100,100,0,100);
	// line(100,0,0,0);
	// line(100,0,100,100);

	// save("enemy_commander.jpg");
	// save("soldier_commander.jpg");

	fill(0,0,0);
	noStroke();
	quad(50, 10, 40, 50, 50, 90, 60, 50);
	quad(10, 50, 50, 40, 90, 50, 50, 60);
	quad(20, 20, 45, 55, 80, 80, 55, 45);
	quad(20, 80, 45, 45, 80, 20, 55, 55);

	// saveFrame("soldier_king.jpg");
	saveFrame("enemy_king.jpg");

}