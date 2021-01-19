Public class Problem{

	public static void main(String[] x){
			System.out.println("Nilai random-Simulasi Coint");
			System.out.println("===========================");
			for (int i=1;i<11;i++){
				double hasillempar=Math.random();
				if (hasillempar<=0.5){
					System.out.println(i+". Angka");
				}else if(hasillempar>0.5){
					System.out.println(i+". Pa Simantupang");
				}

			}
		
		}
}