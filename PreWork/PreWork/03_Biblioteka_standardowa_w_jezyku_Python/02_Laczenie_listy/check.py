from ast import walk, Call, Attribute, Constant
import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), "..", "..")))


from testrunner import CodersLabTestSuite, CodersLabException, p, dedent


tc = CodersLabTestSuite("Łączenie listy")


@tc.test('Zmienna "litery" istnieje i ma oczekiwaną wartość', aborts=True)
def test_variable(invoke, **kwargs):
    variables = invoke()

    if "litery" not in variables:
        raise CodersLabException("Nie znaleziono zmiennej {}".format(p.b.get("litery")))

    if variables["litery"] != ["a", "b", "c", "d", "e"]:
        raise CodersLabException(
            dedent(
                """
                Oczekiwano, że zmienna {} będzie miała wartość {}.
                Jej obecna wartość to {}.
                """
            ).format(
                p.b.get("litery"),
                p.b.get(["a", "b", "c", "d", "e"]),
                p.b.get(variables["litery"]),
            )
        )


@tc.test('Metoda "join" została użyta')
def test_variable(ast, **kwargs):
    for node in walk(ast):
        if (
            isinstance(node, Call)
            and isinstance(node.func, Attribute)
            and node.func.attr == "join"
        ):
            if isinstance(node.func.value, Constant):
                if node.func.value.value == " ":
                    return
                else:
                    raise CodersLabException(
                        dedent(
                            """
                            Zły separator. Aby pomiędzy literami pojawiła się spacja,
                            string który będzie łączył elementy listy musi być spacją.
                            Przykład:
                            {}   ->   {}
                            {}   ->   {}
                            """
                        ).format(
                            p.b.get('".".join(["www", "coderslab", "pl"])'),
                            p.b.get('"www.coderslab.pl"'),
                            p.b.get('" ".join(["Ala", "ma", "kota"])'),
                            p.b.get('"Ala ma kota"'),
                        )
                    )

    raise CodersLabException(
        dedent(
            """
            Nie znaleziono użycia metody {} które było wymagane w tym zadaniu.
            Przykład:
            {}
            {}
            """
        ).format(
            p.b.get("join"),
            p.b.get('>>> print(" && ".join(["A", "B", "CDE"]))'),
            p.b.get("A && B && CDE"),
        )
    )


@tc.test("Napis pojawia się na ekranie")
def test_print(invoke, stdout, **kwargs):
    invoke()

    tc.assert_print_called(stdout)

    if not any("a b c d e" in line for line in stdout):
        raise CodersLabException(
            dedent(
                """
                Nie znaleziono oczekiwanej frazy {} w tekście wypisywanym na ekranie.
                Wypisany tekst:
                {}
                """
            ).format(
                p.b.get("a b c d e"),
                p.b.get("".join(stdout)),
            )
        )


tc.run()
