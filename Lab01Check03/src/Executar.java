import java.io.IOException;

import org.apache.lucene.queryparser.classic.ParseException;


public class Executar {

	public static void main(String[] args) throws IOException, ParseException {
		LuceneTeste oi = new LuceneTeste();
		oi.lerDocs("C:\\Users\\jordan\\Documents\\teste");
		oi.luceneTesteBusca("escritor ingles", 10);

	}

}
