import typing
import pathlib

class Config:
	"""
	Configurations and Helper functions
	"""
	def __init__(self) -> None:
		self.pth: str = pathlib.Path.cwd().parents[0]/"datasets/tep-gnn/JavaTestFiles"
		self.h2: str = self.pth/"H2"
		self.rdf4j: str = self.pth/"rdf4j"
		self.dubbo: str = self.pth/"apache/dubbo"
		self.systemds: str = self.pth/"apache/systemds"
		self.ftr_pth = pathlib.Path.cwd() / "pak-cpp/features/"
		self.nsr_pth = self.ftr_pth / "AB/NSR"
		self.dsr_pth = self.ftr_pth / "AB/DSR"
		self.tgt_pth = self.ftr_pth / "AB/targets"
		self.runtime_c = "Test File;Runtime in ms"
		self.runtime_c_ms = "Runtime in ms"
		self.dubbo_h2 = "dubbo|h2"
		self.rdf4j = "rdf4j"
		self.file_name = "file_name"
		self.runtime_ms = "runtime_ms"
		self.test_case = "Test case"
		self.test_file = "Test File"
		self.max_seqlen: int = 64
		
		self.feature_types: typing.Dict =  {
			"statements" : [
				"IfStatement", "WhileStatement", "DoStatement",
				"AssertStatement", "SwitchStatement", "ForStatement",
				"ContinueStatement", "ReturnStatement", "ThrowStatement",
				"SynchronizedStatement", "TryStatement", "BreakStatement",
				"BlockStatement", "BinaryOperation", "CatchClause"
			],
			"expressions" : [
				"StatementExpression", "TernaryExpression", "LambdaExpression"
			],
			"controls" : [
				"ForControl", "EnhancedForControl"
			],
			"invocations" : [
				"SuperConstructorInvocation", "MethodInvocation",  "SuperMethodInvocation", "SuperMemberReference"
				"ExplicitConstructorInvocation", "ArraySelector", "AnnotationMethod", "MethodReference"
			],
			"declarations" : [
				"TypeDeclaration", "FieldDeclaration", "MethodDeclaration", 
				"ConstructorDeclaration", "PackageDeclaration", "ClassDeclaration", 
				"EnumDeclaration", "InterfaceDeclaration", "AnnotationDeclaration", 
				"ConstantDeclaration", "VariableDeclaration", "LocalVariableDeclaration",
				"EnumConstantDeclaration", "VariableDeclarator"
			]
	}
		
def read_txtfile(file):
	with open(file) as f:
		return f.readlines()

def filter_features(file, l_filter):
	data = [line for line in read_txtfile(file) if line.startswith(l_filter)]
	return list(reversed([float(d.split()[3]) for d in data]))